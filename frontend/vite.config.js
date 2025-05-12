import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': 'http://localhost:5001'
    }
  },
  build: {
    outDir: 'dist', // 设置构建文件的输出目录
    assetsDir: 'assets', // 设置构建静态资源的目录
  },
})
