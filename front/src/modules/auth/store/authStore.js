import { reactive } from "vue"

export const authStore = reactive({
  token: localStorage.getItem("token"),

  user: null,

  get isAuthenticated() {
    return !!this.token
  },

  setToken(token) {
    this.token = token

    localStorage.setItem("token", token)
  },

  logout() {
    this.token = null

    this.user = null

    localStorage.removeItem("token")
  },
})