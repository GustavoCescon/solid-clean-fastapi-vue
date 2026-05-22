import { ref } from "vue"
import { getAddressesByUser, removeAddress } from "../services/addressService"
import { useRequest } from "@/shared/composables/useRequest"

export function useAddresses() {
  const addresses = ref([])

  const { loading, error, execute } = useRequest()

  const fetchAddresses = async (userId) => {
    await execute(async () => {
      addresses.value = await getAddressesByUser(userId)
    })
  }

  const deleteAddress = async (userId, addressId) => {
    await execute(() => removeAddress(userId, addressId))
  }

  return {
    addresses,
    loading,
    error,
    fetchAddresses,
    deleteAddress,
  }
}
