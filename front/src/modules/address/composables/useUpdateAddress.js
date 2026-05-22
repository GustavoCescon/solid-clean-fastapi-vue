import { ref } from "vue"
import { useRouter } from "vue-router"
import { getAddressById, updateAddress } from "../services/addressService"
import { useRequest } from "@/shared/composables/useRequest"

export function useUpdateAddress() {
  const router = useRouter()

  const id = ref(null)
  const userId = ref(null)
  const street = ref("")
  const number = ref("")
  const complement = ref("")
  const neighborhood = ref("")
  const city = ref("")
  const state = ref("")
  const zip_code = ref("")

  const { loading, error, execute } = useRequest()

  const loadAddress = async (uId, addressId) => {
    userId.value = uId
    id.value = addressId
    const data = await getAddressById(uId, addressId)
    street.value = data.street
    number.value = data.number
    complement.value = data.complement || ""
    neighborhood.value = data.neighborhood
    city.value = data.city
    state.value = data.state
    zip_code.value = data.zip_code
  }

  const update = async () => {
    await execute(async () => {
      await updateAddress(userId.value, id.value, {
        street: street.value,
        number: number.value,
        complement: complement.value || null,
        neighborhood: neighborhood.value,
        city: city.value,
        state: state.value,
        zip_code: zip_code.value.replace(/\D/g, ""),
      })
      router.push(`/users/${userId.value}/addresses`)
    })
  }

  return {
    street, number, complement, neighborhood, city, state, zip_code,
    loading, error, loadAddress, update,
  }
}
