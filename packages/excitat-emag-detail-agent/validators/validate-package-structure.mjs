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
  'data/component-cards.json',
  'data/gif-component-usage-cards.json',
  'data/guard-pipeline.json',
  'data/stable-component-catalog.json',
  'data/detail-module-catalog.json',
  'components/EMAG_COMPATIBILITY.md',
  'components/COMPONENT_APPLICATION_SOP.md',
  'components/BENCHMARK_CAPABILITY_MAP.md',
  'components/gif-motion/component-candidates.md',
  'components/micro-labels/README.md',
  'image-workflow/IMAGE_PROMPT_CONTRACT.md',
  'image-workflow/GIF_SCALE_WORKFLOW.md',
  'image-workflow/provider-profiles/openai-gpt-image.md',
  'image-workflow/provider-profiles/nanobanana2.md',
  'assembly/route-policies/stable-listing.md',
  'assembly/route-policies/premium-listing.md',
  'assembly/blueprints/default-stable-detail.json',
  'assembly/blueprints/premium-hero-plus-components.json',
  'renderers/gif-motion-renderer.py',
  'spec/state-design.json',
  'spec/template-selection.json',
  'spec/chat-plan.md',
  'spec/chart-specs.json',
  'spec/evidence-index.json',
  'spec/media-asset-index.json',
  'spec/qa-report.json',
  'spec/repair-plan.md',
  'spec/execute-report.json',
  'examples/component-gallery/gif-motion-html-preview.html',
  'examples/d6mhw43bm-component-application/demo.html',
  'examples/d6mhw43bm-component-application/benchmark-push-demo.html',
  'examples/d6mhw43bm-component-application/adapted-gif-component-gallery.html',
  'examples/d6mhw43bm-component-application/adapted-listing-flow-demo.html',
  'examples/d6mhw43bm-component-application/media_asset_index.json',
  'validators/validate-emag-detail-html.py'
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

const cardPath = join(root, 'data/component-cards.json');
if (existsSync(cardPath)) {
  const cardDeck = JSON.parse(readFileSync(cardPath, 'utf8'));
  const requiredCardFields = [
    'component_id',
    'component_name',
    'tags',
    'listing_modules',
    'source_code',
    'usage_guide',
    'emag_compatibility',
    'stability_tier',
    'failure_modes'
  ];
  const ids = new Set();
  for (const card of cardDeck.cards ?? []) {
    if (ids.has(card.component_id)) {
      failures.push(`duplicate component card: ${card.component_id}`);
    }
    ids.add(card.component_id);
    for (const field of requiredCardFields) {
      if (!(field in card)) {
        failures.push(`component card ${card.component_id ?? '<unknown>'} missing field ${field}`);
      }
    }
    if (!Array.isArray(card.tags) || card.tags.length === 0) {
      failures.push(`component card ${card.component_id ?? '<unknown>'} must include tags`);
    }
    if (!Array.isArray(card.listing_modules) || card.listing_modules.length === 0) {
      failures.push(`component card ${card.component_id ?? '<unknown>'} must include listing_modules`);
    }
    if (!card.source_code?.production_embed) {
      failures.push(`component card ${card.component_id ?? '<unknown>'} missing source_code.production_embed`);
    }
  }
  if ((cardDeck.cards ?? []).length < 16) {
    failures.push('component-cards.json should include at least 16 first-batch candidates');
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
