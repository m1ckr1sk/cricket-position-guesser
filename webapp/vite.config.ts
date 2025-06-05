import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    cors: true,
    proxy: {
      '/game': {
        rewrite: (path) => path.replace(/^\/game/, ''),
        target: 'http://127.0.0.1:8000/game',
        changeOrigin: true,
        secure: false,
        ws: true
      },
      '/guess': {
        rewrite: (path) => path.replace(/^\/guess/, ''),
        target: 'http://127.0.0.1:8000/game/guess',
        changeOrigin: true,
        secure: false,
        ws: true,
        followRedirects: true
      },
    }
  },
})
