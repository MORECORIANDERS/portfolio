import { defineConfig } from 'astro/config';

// 部署于 https://morecorianders.github.io/portfolio/
export default defineConfig({
  site: 'https://morecorianders.github.io',
  base: '/portfolio/',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
});
