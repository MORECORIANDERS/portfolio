import { defineConfig } from 'astro/config';

// 部署于 Vercel
export default defineConfig({
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
