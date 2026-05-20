import { ref } from "vue"

import { useAuth } from "./useAuth"

export function useRegisterForm() {
  const login = ref("")
  const email = ref("")
  const password = ref("")

  const {
    signUp,
    loading,
    error,
  } = useAuth()

  const submit = async () => {
    await signUp(
      login.value,
      email.value,
      password.value,
    )
  }

  return {
    login,
    email,
    password,

    loading,
    error,

    submit,
  }
}