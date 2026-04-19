# ============================================================================
# MANYA REACT ASSETS - Automated Release & Versioning Script
# ============================================================================
# This script automates:
# 1. Version bumping (patch/minor/major)
# 2. Git tagging
# 3. GitHub pushing
# 4. jsDelivr cache purging
# ============================================================================

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('patch', 'minor', 'major')]
    [string]$BumpType = 'patch',
    
    [Parameter(Mandatory=$false)]
    [string]$Message = '',
    
    [Parameter(Mandatory=$false)]
    [bool]$SkipPush = $false,
    
    [Parameter(Mandatory=$false)]
    [bool]$SkipPurge = $false
)

# Helper functions for output
$ErrorActionPreference = 'Stop'

function Write-Header {
    param([string]$Text)
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host $Text -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Text)
    Write-Host "✓ $Text" -ForegroundColor Green
}

function Write-Info {
    param([string]$Text)
    Write-Host "ℹ $Text" -ForegroundColor Blue
}

function Write-ErrorMsg {
    param([string]$Text)
    Write-Host "✗ $Text" -ForegroundColor Red
}

# Main script
Write-Header "MANYA ASSETS - Release Automation"

# Check if package.json exists
if (-not (Test-Path "package.json")) {
    Write-ErrorMsg "package.json not found in current directory!"
    exit 1
}

# Read current version from package.json
$packageJson = Get-Content "package.json" -Raw | ConvertFrom-Json
$currentVersion = $packageJson.version
Write-Info "Current version: $currentVersion"

# Parse version components
$versionParts = $currentVersion -split '\.'
$major = [int]$versionParts[0]
$minor = [int]$versionParts[1]
$patch = [int]$versionParts[2]

# Calculate new version
switch ($BumpType) {
    'major' {
        $major++
        $minor = 0
        $patch = 0
    }
    'minor' {
        $minor++
        $patch = 0
    }
    'patch' {
        $patch++
    }
}

$newVersion = "$major.$minor.$patch"
Write-Info "New version: $newVersion"

# Create release message
if (-not $Message) {
    $defaultMsg = "Release v$newVersion - " + (Get-Date -Format "yyyy-MM-dd")
    Write-Info "Release message: $defaultMsg"
    $Message = $defaultMsg
} else {
    Write-Info "Release message: $Message"
}

# Step 1: Update package.json
Write-Header "Step 1: Updating package.json"
try {
    $packageJson.version = $newVersion
    $packageJson | ConvertTo-Json -Depth 10 | Set-Content "package.json"
    Write-Success "Updated package.json to version $newVersion"
} catch {
    Write-ErrorMsg "Failed to update package.json: $_"
    exit 1
}

# Step 2: Git add and commit
Write-Header "Step 2: Git Commit"
try {
    git add package.json
    git commit -m "chore: bump version to $newVersion"
    Write-Success "Git commit created"
} catch {
    Write-ErrorMsg "Failed to commit: $_"
    exit 1
}

# Step 3: Create Git tag
Write-Header "Step 3: Creating Git Tag"
try {
    git tag -a "v$newVersion" -m "$Message"
    Write-Success "Git tag v$newVersion created"
} catch {
    Write-ErrorMsg "Failed to create tag: $_"
    exit 1
}

# Step 4: Push to GitHub
if (-not $SkipPush) {
    Write-Header "Step 4: Pushing to GitHub"
    try {
        Write-Info "Pushing commits..."
        git push origin main
        Write-Success "Commits pushed"
        
        Write-Info "Pushing tags..."
        git push origin --tags
        Write-Success "Tags pushed"
    } catch {
        Write-ErrorMsg "Failed to push: $_"
        exit 1
    }
} else {
    Write-Info "Skipping push (--SkipPush flag set)"
}

# Step 5: Purge jsDelivr cache
if (-not $SkipPurge) {
    Write-Header "Step 5: Purging jsDelivr Cache"
    try {
        $purgeUrl = "https://purge.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/"
        Write-Info "Purging cache for: $purgeUrl"
        
        $response = Invoke-WebRequest -Uri $purgeUrl -Method POST -ErrorAction Stop
        
        if ($response.StatusCode -eq 200 -or $response.StatusCode -eq 404) {
            Write-Success "jsDelivr cache purged successfully"
        }
    } catch {
        Write-Information "Warning: jsDelivr purge may have failed: $_" -InformationAction Continue
        Write-Info "You can manually purge at: https://purge.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/"
    }
} else {
    Write-Info "Skipping jsDelivr purge (--SkipPurge flag set)"
}

# Step 6: Generate CDN URLs
Write-Header "Step 6: CDN URLs Ready"
Write-Info "Use these URLs for your assets:"
Write-Host "`nAssets (replace {asset-path} with your path):" -ForegroundColor Yellow
Write-Host "https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/{asset-path}" -ForegroundColor White

Write-Host "`nExamples:" -ForegroundColor Yellow
Write-Host "GLB Models:" -ForegroundColor Yellow
Write-Host "https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/assets/science/musklo-skeletal-system/quest_2_human_skeleton/male_skeleton_compressed.glb" -ForegroundColor White

Write-Host "`nImages:" -ForegroundColor Yellow
Write-Host "https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/assets/science/musklo-skeletal-system/quest_8_hinge_ball-and-socket/elbow_image.webp" -ForegroundColor White

Write-Host "`nJSON Configs:" -ForegroundColor Yellow
Write-Host "https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v$newVersion/content/science/musklo-skeletal-system/quest_4_axial_rib_cage/labeling_v3.json" -ForegroundColor White

# Step 7: Create GitHub Release (instructions)
Write-Header "Step 7: Create GitHub Release (Manual)"
Write-Info "Visit: https://github.com/manyaug/manya-react-assets/releases/new"
Write-Info "Tag: v$newVersion"
Write-Info "Title: Release v$newVersion"
Write-Info "Description: $Message"

Write-Header "Release Complete!"
Write-Success "Version $newVersion is now live on jsDelivr!"
Write-Info "Cache should refresh within 5-10 minutes"
