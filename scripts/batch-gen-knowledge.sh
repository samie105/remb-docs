#!/usr/bin/env bash
set -euo pipefail
cd /root/remb-docs

SLUGS="astro bun deno drizzle fastify hono nextjs postgres prisma react redis supabase svelte tailwind trpc vite"
LOG="/root/remb-docs/state/runs/knowledge-batch-$(date +%Y%m%d-%H%M%S).log"

echo "=== Batch knowledge generation started at $(date) ===" > "$LOG"
for slug in $SLUGS; do
    echo "[>>> $slug]" | tee -a "$LOG"
    if python3 scripts/gen-rich-knowledge.py "$slug" >> "$LOG" 2>&1; then
        echo "[OK $slug]" | tee -a "$LOG"
    else
        echo "[FAILED $slug exit $?]" | tee -a "$LOG"
    fi
    sleep 2
done
echo "=== Batch finished at $(date) ===" >> "$LOG"
echo "All done. Log: $LOG"
