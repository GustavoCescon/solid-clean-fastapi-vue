import api from "@/shared/api/http"
import { AppError } from "@/shared/errors/AppError"

export async function getAddressesByUser(userId) {
  try {
    const res = await api.get(`/users/${userId}/addresses`)
    return res.data
  } catch (error) {
    throw new AppError(
      error.response?.data?.error || "Erro ao buscar endereços",
      error.response?.status
    )
  }
}

export async function createAddress(userId, payload) {
  try {
    const res = await api.post(`/users/${userId}/addresses`, payload)
    return res.data
  } catch (error) {
    throw new AppError(
      error.response?.data?.error || "Erro ao criar endereço",
      error.response?.status
    )
  }
}

export async function getAddressById(userId, addressId) {
  const res = await api.get(`/users/${userId}/addresses/${addressId}`)
  return res.data
}

export async function updateAddress(userId, addressId, payload) {
  const res = await api.put(`/users/${userId}/addresses/${addressId}`, payload)
  return res.data
}

export async function removeAddress(userId, addressId) {
  const res = await api.delete(`/users/${userId}/addresses/${addressId}`)
  return res.data
}
