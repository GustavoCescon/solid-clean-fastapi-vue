import { ref } from "vue"
import { useRouter } from "vue-router"
import { createAddress } from "../services/addressService"
import { useRequest } from "@/shared/composables/useRequest"

export function useCreateAddressForm(userId) {
  const router = useRouter()

  const street = ref("")
  const number = ref("")
  const complement = ref("")
  const neighborhood = ref("")
  const city = ref("")
  const state = ref("")
  const zip_code = ref("")

  const { loading, error, execute } = useRequest()

  const submit = async () => {
    await execute(async () => {
      await createAddress(userId, {
        street: street.value,
        number: number.value,
        complement: complement.value || null,
        neighborhood: neighborhood.value,
        city: city.value,
        state: state.value,
        zip_code: zip_code.value.replace(/\D/g, ""),
      })
      router.push(`/users/${userId}/addresses`)
    })
  }

  return {
    street, number, complement, neighborhood, city, state, zip_code,
    loading, error, submit,
  }
}
