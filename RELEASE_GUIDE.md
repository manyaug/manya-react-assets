# 🚀 Release & Versioning Guide

## Quick Start

### Option 1: Using npm scripts (easiest)
```powershell
npm run release:patch   # v1.0.0 → v1.0.1 (bug fixes)
npm run release:minor   # v1.0.0 → v1.1.0 (new features/assets)
npm run release:major   # v1.0.0 → v2.0.0 (breaking changes)
```

### Option 2: Using PowerShell directly
```powershell
# Patch release (bug fixes, typos, image updates)
powershell -File release.ps1 -BumpType patch

# Minor release (new quests, new images, new content)
powershell -File release.ps1 -BumpType minor

# Major release (significant restructuring, major updates)
powershell -File release.ps1 -BumpType major

# Custom message
powershell -File release.ps1 -BumpType patch -Message "Fixed GLB paths and image references"
```

### Option 3: Skip certain steps
```powershell
# Skip pushing to GitHub (test locally first)
powershell -File release.ps1 -BumpType patch -SkipPush $true

# Skip jsDelivr cache purge (purge manually)
powershell -File release.ps1 -BumpType patch -SkipPurge $true
```

---

## What The Script Does

✅ **Automatically:**
1. Reads current version from `package.json`
2. Bumps version (patch/minor/major)
3. Updates `package.json`
4. Creates git commit
5. Creates git tag (v1.0.0, v1.0.1, etc.)
6. Pushes commits and tags to GitHub
7. Purges jsDelivr cache
8. Displays CDN URLs for all your assets

---

## After Release

### Create GitHub Release (Manual - takes 30 seconds)
1. Go to: https://github.com/manyaug/manya-react-assets/releases/new
2. Use the tag that was just created (e.g., `v1.0.1`)
3. Add description of what changed
4. Click "Publish release"

### Update Your Application URLs

**Before (cached version):**
```javascript
https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@main/assets/science/...
```

**After (specific version - no cache issues):**
```javascript
https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v1.0.1/assets/science/...
```

---

## Common Use Cases

### After updating GLB files
```powershell
npm run release:patch
# or
powershell -File release.ps1 -BumpType patch -Message "Updated science GLB models - Quests 1-14"
```

### After adding new images
```powershell
npm run release:patch
# v1.0.0 → v1.0.1
```

### After adding entire new subject or major overhaul
```powershell
npm run release:minor
# v1.0.0 → v1.1.0
```

### Breaking changes (different structure)
```powershell
npm run release:major
# v1.0.0 → v2.0.0
```

---

## Monitor CDN Performance

Check if files are served from cache:
```powershell
curl -I "https://cdn.jsdelivr.net/gh/manyaug/manya-react-assets@v1.0.1/assets/science/..."
```

Look for `x-cache: HIT` header = working from cache (fast ⚡)

---

## Troubleshooting

### Script fails: "git not found"
```powershell
# Make sure Git is installed and in PATH
git --version
```

### jsDelivr still showing old files after 10 minutes
```powershell
# Manually purge (copy URL from script output)
Invoke-WebRequest -Uri "https://purge.jsdelivr.net/gh/manyaug/manya-react-assets@v1.0.1/" -Method POST
```

### Need to undo a release
```powershell
# Delete local tag
git tag -d v1.0.1

# Delete remote tag
git push origin --delete v1.0.1

# Roll back version in package.json manually
```

---

## Version History

| Version | Released | Changes |
|---------|----------|---------|
| v1.0.0 | 2026-04-13 | Initial release - Fixed GLB and image paths |
| v1.0.1+ | TBD | Future updates |

---

## Questions?

Check the release.ps1 script for advanced options or modify it for your needs!
