import { defineConfig } from 'vite'
import { resolve } from 'path'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/',
  resolve: {
    alias: {
      '@': resolve(',/src'),
      '@img': resolve('./src/assets/img'),
    },
  },
  server: {
    port: 8080,
    open: true,
    proxy: {
      
    }
  }
})
