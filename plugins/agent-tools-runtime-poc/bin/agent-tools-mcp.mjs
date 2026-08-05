#!/usr/bin/env node

import { spawn } from 'node:child_process';

const packageSpec = '@rckflr/agent-tools-runtime@0.1.1';
const localServer = new URL('../runtime/mcp-server.mjs', import.meta.url);

function runLocal() {
  process.env.AGENT_TOOLS_RUNTIME_SOURCE = 'local';
  import(localServer.href);
}

if (process.env.AGENT_TOOLS_RUNTIME_SOURCE === 'local') {
  runLocal();
} else {
  const executable = process.platform === 'win32' ? 'npx.cmd' : 'npx';
  const child = spawn(executable, ['--yes', '--package', packageSpec, 'agent-tools-mcp'], {
    stdio: 'inherit',
    env: { ...process.env, npm_config_ignore_scripts: 'true' },
    windowsHide: true,
  });
  child.once('error', runLocal);
  child.once('exit', (code) => {
    if (code !== 0) runLocal();
  });
}
