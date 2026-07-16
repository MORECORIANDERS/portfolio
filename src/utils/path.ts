// 处理静态资源引用的 base 路径（跟随 Astro config 中的 base 配置）
const BASE = import.meta.env.BASE_URL;

/** 将 frontmatter 中的资源路径转换为带 base 的最终路径 */
export function asset(path: string): string {
  const clean = path.replace(/^\/+/, '');
  return `${BASE}${clean}`;
}
