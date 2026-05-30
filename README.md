# Two Pointers, One Repo

This repository tracks my Data Structures and Algorithms (DSA) progression using a monorepo approach. It acts as a single source of truth for both my automated submissions and my manual sandbox testing.

## 📂 Repository Structure

The code here converges from two distinct sources:

* **`/leetcode-sync`**: The automated pointer. This directory is managed by a GitHub Action that automatically fetches and commits my successful LeetCode submissions, preserving problem descriptions and performance metrics.
* **`/manual-practice`**: The human pointer. This directory contains raw code, brute-force attempts, and custom data structure implementations tested locally before hitting the platform.

## 🛠️ Stack & Automation
* **Language:** Python mainly, java, js too {maybe}
* **CI/CD:** GitHub Actions (LeetCode Sync workflow)
* **Manual Commits:** also doing casual practises and pushing them casually