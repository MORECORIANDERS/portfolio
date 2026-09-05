import { defineConfig } from 'astro/config';

// 部署于 GitHub Pages，子路径 /portfolio/
export default defineConfig({
  base: '/portfolio',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
