import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('..', import.meta.url).pathname;

const requiredPaths = [
  'README.md',
  'DESIGN.md',
  'DESIGN_FD.md',
  'SKILL.md',
  'agent-profile.json',
  'data/component-registry.json',
  'data/guard-pipeline.json',
  'data/stable-component-catalog.json',
  'data/detail-module-catalog.json',
  'components/gif-motion/component-candidates.md',
  'components/micro-labels/README.md',
  'image-workflow/IMAGE_PROMPT_CONTRACT.md',
  'image-workflow/provider-profiles/openai-gpt-image.md',
  'image-workflow/provider-profiles/nanobanana2.md',
  'assembly/route-policies/stable-listing.md',
  'assembly/route-policies/premium-listing.md',
  'assembly/blueprints/default-stable-detail.json',
  'assembly/blueprints/premium-hero-plus-components.json',
  'spec/state-design.json',
  'spec/template-selection.json',
  'spec/chat-plan.md',
  'spec/chart-specs.json',
  'spec/evidence-index.json',
  'spec/media-asset-index.json',
  'spec/qa-report.json',
  'spec/repair-plan.md',
  'spec/execute-report.json',
  'examples/component-gallery/gif-motion-html-preview.html'
];

const failures = [];

for (const rel of requiredPaths) {
  if (!existsSync(join(root, rel))) {
    failures.push(`missing required path: ${rel}`);
  }
}

const registryPath = join(root, 'data/component-registry.json');
if (existsSync(registryPath)) {
  const registry = JSON.parse(readFileSync(registryPath, 'utf8'));
  for (const component of registry.initial_components ?? []) {
    for (const field of registry.required_component_fields ?? []) {
      if (!(field in component)) {
        failures.push(`component ${component.component_id ?? '<unknown>'} missing field ${field}`);
      }
    }
  }
}

const premiumPath = join(root, 'assembly/blueprints/premium-hero-plus-components.json');
if (existsSync(premiumPath)) {
  const premium = JSON.parse(readFileSync(premiumPath, 'utf8'));
  if (premium.max_image_jobs !== 2) {
    failures.push('premium blueprint must cap max_image_jobs at 2');
  }
}

const stablePath = join(root, 'assembly/blueprints/default-stable-detail.json');
if (existsSync(stablePath)) {
  const stable = JSON.parse(readFileSync(stablePath, 'utf8'));
  if (stable.image_generation_allowed !== false) {
    failures.push('stable blueprint must disallow image generation');
  }
}

const promptContractPath = join(root, 'image-workflow/IMAGE_PROMPT_CONTRACT.md');
if (existsSync(promptContractPath)) {
  const promptContract = readFileSync(promptContractPath, 'utf8');
  for (const phrase of ['no readable text', 'no fake badge', 'no distorted product']) {
    if (!promptContract.includes(phrase)) {
      failures.push(`prompt contract missing phrase: ${phrase}`);
    }
  }
}

if (failures.length > 0) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log('EXCITAT eMAG Detail Agent package structure: pass');
