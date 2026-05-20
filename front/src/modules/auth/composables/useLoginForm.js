import { ref } from "vue"

import { useAuth } from "./useAuth"

export function useLoginForm() {
  const email = ref("")

  const password = ref("")

  const {
    signIn,
    loading,
    error,
  } = useAuth()

  const submit = async () => {
    await signIn(
      email.value,
      password.value,
    )
  }

  return {
    email,
    password,

    loading,
    error,

    submit,
  }
}