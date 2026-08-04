param(
  [Parameter(Mandatory = $true)][string]$HostName,
  [Parameter(Mandatory = $true)][string]$UserName,
  [int]$Port = 22,
  [string]$IdentityFile
)

$ErrorActionPreference = 'Stop'
$ssh = Get-Command ssh -ErrorAction SilentlyContinue
$keyExists = [string]::IsNullOrWhiteSpace($IdentityFile) -or (Test-Path -LiteralPath $IdentityFile -PathType Leaf)
$knownHosts = Join-Path $HOME '.ssh\known_hosts'

[pscustomobject]@{
  ssh_available = $null -ne $ssh
  ssh_path = if ($ssh) { $ssh.Source } else { $null }
  host = $HostName
  user = $UserName
  port = $Port
  identity_file_supplied = -not [string]::IsNullOrWhiteSpace($IdentityFile)
  identity_file_exists = $keyExists
  known_hosts_exists = Test-Path -LiteralPath $knownHosts -PathType Leaf
  ready_for_host_key_inspection = ($null -ne $ssh) -and $keyExists
} | ConvertTo-Json -Depth 3
