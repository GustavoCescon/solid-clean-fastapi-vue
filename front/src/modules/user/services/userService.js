import api from "@/shared/api/http"

import { AppError } from "@/shared/errors/AppError"

export async function getUsers({ page = 1, size = 10 } = {}) {
  try {
    const response = await api.get("/users", { params: { page, size } })

    return response.data
  } catch (error) {
    throw new AppError(
      error.response?.data?.error ||
        "Erro ao buscar usuários",
      error.response?.status
    )
  }
}

export async function createUser(payload) {
  try {
    const response = await api.post(
      "/users",
      payload
    )

    return response.data
  } catch (error) {
    throw new AppError(
      error.response?.data?.error ||
        "Erro ao criar usuário",
      error.response?.status
    )
  }
}

export async function getUserById(id) {
  const res = await api.get(`/users/${id}`)
  return res.data
}

export async function updateUser(id, payload) {
  const res = await api.put(`/users/${id}`, payload)
  return res.data
}

export async function removeUserById(id) {
  const res = await api.delete(`/users/${id}`)
  return res.data
}