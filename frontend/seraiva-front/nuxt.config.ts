// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@sidebase/nuxt-auth'
  ],
  css:[
    '~/assets/style/global-project.scss',
    '~/assets/style/global-variables.scss'
  ],
  auth: {
    baseURL: 'http://seraiva-somativa-production.up.railway.app',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        getSession: { path: '/users', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/login' }
    }
  }
})
