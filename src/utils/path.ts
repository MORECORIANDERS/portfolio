// 处理 GitHub Pages 子路径 base（/portfolio/）下的静态资源引用
const BASE = import.meta.env.BASE_URL; // 例如 '/portfolio/'

/** 将 frontmatter 中的资源路径转换为带 base 的最终路径 */
export function asset(path: string): string {
  const clean = path.replace(/^\/+/, '');
  return `${BASE}${clean}`;
}
