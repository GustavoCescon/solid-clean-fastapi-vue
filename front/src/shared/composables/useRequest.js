import { ref } from "vue"

export function useRequest() {
  const loading = ref(false)

  const error = ref(null)

  const execute = async (callback) => {
    loading.value = true

    error.value = null

    try {
      return await callback()
    } catch (err) {
      error.value =
        err?.response?.data?.detail ||
        err.message ||
        "Erro inesperado"

      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    loading,
    error,
    execute,
  }
}