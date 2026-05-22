<template>
  <AppLayout>

    <div class="mb-6">
      <BaseButton
        icon="pi pi-arrow-left"
        label="Voltar"
        text
        size="small"
        class="mb-3"
        @click="router.push(`/users/${userId}/addresses`)"
      />
      <h1 class="text-2xl font-bold text-surface-900">Novo Endereço</h1>
      <p class="text-surface-500 text-sm mt-0.5">Preencha os dados do endereço</p>
    </div>

    <Card class="max-w-2xl">
      <template #content>
        <Message v-if="error" severity="error" :closable="false" class="mb-4">{{ error }}</Message>
        <AddressForm
          :street="street"
          :number="number"
          :complement="complement"
          :neighborhood="neighborhood"
          :city="city"
          :state="state"
          :zip_code="zip_code"
          :loading="loading"
          @update:street="street = $event"
          @update:number="number = $event"
          @update:complement="complement = $event"
          @update:neighborhood="neighborhood = $event"
          @update:city="city = $event"
          @update:state="state = $event"
          @update:zip_code="zip_code = $event"
          @submit="submit"
          @cancel="router.push(`/users/${userId}/addresses`)"
        />
      </template>
    </Card>

  </AppLayout>
</template>

<script setup>
import { computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import AppLayout from "@/shared/components/layout/AppLayout.vue"
import AddressForm from "../components/AddressForm.vue"
import Card from "primevue/card"
import BaseButton from "@/shared/components/base/BaseButton.vue"
import Message from "primevue/message"
import { useCreateAddressForm } from "../composables/useCreateAddressForm"

const route = useRoute()
const router = useRouter()
const userId = computed(() => Number(route.params.userId))

const {
  street, number, complement, neighborhood, city, state, zip_code,
  loading, error, submit,
} = useCreateAddressForm(userId.value)
</script>
