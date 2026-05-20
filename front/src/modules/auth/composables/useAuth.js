import { useRouter } from "vue-router"

import { login, register } from "../services/authService"

import { authStore } from "../store/authStore"

import { useRequest } from "@/shared/composables/useRequest"

export function useAuth() {
  const router = useRouter()

  const {
    loading,
    error,
    execute,
  } = useRequest()

  const signIn = async (email, password) => {
    const response = await execute(() =>
      login({
        email,
        password,
      })
    )

    authStore.setToken(response.access_token)

    router.push("/users")
  }
  const signUp = async (login, email, password) => {
    await execute(() =>
      register({
        login,
        email,
        password,
      })
    )

    router.push("/login")
  }

  const logout = () => {
    authStore.logout()

    router.push("/login")
  }

  return {
    loading,
    error,

    signIn,
    signUp,
    logout,

    authStore,
  }
}