#!/usr/bin/env node

async function start() {
  if (process.env.AGENT_TOOLS_RUNTIME_SOURCE !== 'local') {
    try {
      const runtime = await import('@rckflr/agent-tools-runtime/runtime/agent-tools-runtime.mjs');
      await runtime.main();
      return;
    } catch {
      // Fall back to the bundled runtime when the package is unavailable.
    }
  }
  const runtime = await import('../runtime/agent-tools-runtime.mjs');
  await runtime.main();
}

await start();
