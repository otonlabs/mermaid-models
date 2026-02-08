#!/usr/bin/env bash
# Validates Mermaid .mmd files using @mermaid-js/mermaid-cli
# Usage: bash validate_mermaid.sh [models_dir] [sample_size]

set -euo pipefail

MODELS_DIR="${1:-models}"
SAMPLE_SIZE="${2:-50}"
ERRORS=0
CHECKED=0
TOTAL=$(find "$MODELS_DIR" -name "*.mmd" | wc -l | tr -d ' ')

echo "============================================"
echo "Mermaid Validation"
echo "============================================"
echo "Total .mmd files found: $TOTAL"
echo "Validating random sample of: $SAMPLE_SIZE"
echo ""

# Check if mmdc is available
if ! npx mmdc --version &>/dev/null; then
    echo "Installing @mermaid-js/mermaid-cli..."
    npm install -g @mermaid-js/mermaid-cli
fi

# Get random sample
FILES=$(find "$MODELS_DIR" -name "*.mmd" | sort -R | head -n "$SAMPLE_SIZE")

for f in $FILES; do
    CHECKED=$((CHECKED + 1))
    if npx mmdc -i "$f" -o /dev/null 2>/dev/null; then
        echo "  OK: $f"
    else
        echo "  FAIL: $f"
        ERRORS=$((ERRORS + 1))
    fi
done

echo ""
echo "============================================"
echo "Results: $CHECKED checked, $ERRORS errors"
echo "============================================"

# Distribution check
echo ""
echo "Distribution by C4 level:"
for level in context container component; do
    COUNT=$(find "$MODELS_DIR" -path "*/$level/*.mmd" | wc -l | tr -d ' ')
    echo "  $level: $COUNT"
done

echo ""
echo "Distribution by cloud:"
for cloud in aws azure gcp oracle-cloud; do
    COUNT=$(find "$MODELS_DIR" -path "*/$cloud/*/*.mmd" | wc -l | tr -d ' ')
    echo "  $cloud: $COUNT"
done

echo ""
echo "Distribution by domain (top 10):"
find "$MODELS_DIR" -name "*.mmd" | awk -F/ '{print $2}' | sort | uniq -c | sort -rn | head -10

if [ "$ERRORS" -gt 0 ]; then
    echo ""
    echo "WARNING: $ERRORS files failed validation."
    exit 1
else
    echo ""
    echo "SUCCESS: All $CHECKED sampled files are valid."
fi
