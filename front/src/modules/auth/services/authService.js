import api from "@/shared/api/http"

import { AppError } from "@/shared/errors/AppError"

export async function login(payload) {
  try {
    const response = await api.post("/auth/login", payload)

    return response.data
  } catch (error) {
    throw new AppError(
      error.response?.data?.detail || "Erro ao realizar login",
      error.response?.status
    )
  }
}

export async function register(payload) {
  try {
    const res = await api.post("/auth/register", payload)
    return res.data
  } catch (error) {
    throw new AppError(error.response?.data?.detail || "Erro ao criar conta",  error.response?.status)
  }
}