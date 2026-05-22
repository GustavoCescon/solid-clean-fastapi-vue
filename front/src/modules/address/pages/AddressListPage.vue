<template>
  <AppLayout>

    <ConfirmDialog />

    <div class="flex items-center justify-between mb-6">
      <div>
        <BaseButton
          icon="pi pi-arrow-left"
          label="Voltar"
          text
          size="small"
          class="mb-3"
          @click="router.push('/users')"
        />
        <h1 class="text-2xl font-bold text-surface-900">Endereços do usuário</h1>
        <p class="text-surface-500 text-sm mt-0.5">Gerencie os endereços cadastrados</p>
      </div>
      <BaseButton
        label="Novo endereço"
        icon="pi pi-plus"
        @click="router.push(`/users/${userId}/addresses/create`)"
      />
    </div>

    <Card>
      <template #content>

        <div v-if="loading" class="flex justify-center py-16">
          <ProgressSpinner />
        </div>

        <Message v-else-if="error" severity="error" :closable="false">{{ error }}</Message>

        <template v-else>
          <Message v-if="addresses.length === 0" severity="info" :closable="false">
            Nenhum endereço cadastrado
          </Message>
          <AddressesTable
            v-else
            :addresses="addresses"
            @edit="goToEdit"
            @delete="confirmDelete"
          />
        </template>

      </template>
    </Card>

  </AppLayout>
</template>

<script setup>
import { onMounted, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import AppLayout from "@/shared/components/layout/AppLayout.vue"
import AddressesTable from "../components/AddressesTable.vue"
import BaseButton from "@/shared/components/base/BaseButton.vue"
import ProgressSpinner from "primevue/progressspinner"
import Message from "primevue/message"
import ConfirmDialog from "primevue/confirmdialog"
import Card from "primevue/card"
import { useAddresses } from "../composables/useAddresses"
import { useConfirm } from "primevue/useconfirm"

const route = useRoute()
const router = useRouter()
const confirm = useConfirm()
const userId = computed(() => Number(route.params.userId))

const { addresses, loading, error, fetchAddresses, deleteAddress } = useAddresses()

onMounted(() => fetchAddresses(userId.value))

const goToEdit = (id) => router.push(`/users/${userId.value}/addresses/${id}/edit`)

const confirmDelete = (id) => {
  confirm.require({
    message: "Deseja realmente deletar este endereço?",
    header: "Confirmação",
    icon: "pi pi-exclamation-triangle",
    acceptSeverity: "danger",
    acceptLabel: "Deletar",
    rejectLabel: "Cancelar",
    accept: async () => {
      await deleteAddress(userId.value, id)
      await fetchAddresses(userId.value)
    },
    reject: () => {},
  })
}
</script>
