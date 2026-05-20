<template>
  <AppLayout>

    <ConfirmDialog />

    <!-- Header -->
    <div class="flex items-center justify-between mb-6">
      <div>
        <h1 class="text-2xl font-bold text-surface-900">Usuários</h1>
        <p class="text-surface-500 text-sm mt-0.5">Gerencie os usuários do sistema</p>
      </div>
      <BaseButton
        label="Novo usuário"
        icon="pi pi-plus"
        @click="router.push('/users/create')"
      />
    </div>

    <!-- Content -->
    <Card>
      <template #content>

        <div v-if="loading" class="flex justify-center py-16">
          <ProgressSpinner />
        </div>

        <Message v-else-if="error" severity="error" :closable="false">
          {{ error }}
        </Message>

        <template v-else>
          <Message v-if="users.length === 0" severity="info" :closable="false">
            Nenhum usuário encontrado
          </Message>
          <UsersTable
            v-else
            :users="users"
            :total="total"
            :size="size"
            @edit="goToEdit"
            @delete="confirmDelete"
            @page="onPage"
          />
        </template>

      </template>
    </Card>

  </AppLayout>
</template>

<script setup>
import { onMounted } from "vue"
import { useRouter } from "vue-router"

import AppLayout from "@/shared/components/layout/AppLayout.vue"
import UsersTable from "../components/UsersTable.vue"

import BaseButton from "@/shared/components/base/BaseButton.vue"
import ProgressSpinner from "primevue/progressspinner"
import Message from "primevue/message"
import ConfirmDialog from "primevue/confirmdialog"
import Card from "primevue/card"

import { useUsers } from "../composables/useUsers"
import { useConfirm } from "primevue/useconfirm"

const router = useRouter()
const confirm = useConfirm()

const { users, total, size, loading, error, fetchUsers, onPage, deleteUser } = useUsers()

onMounted(fetchUsers)

const goToEdit = (id) => router.push(`/users/${id}/edit`)

const confirmDelete = (id) => {
  confirm.require({
    message: "Deseja realmente deletar este usuário?",
    header: "Confirmação",
    icon: "pi pi-exclamation-triangle",
    acceptSeverity: "danger",
    acceptLabel: "Deletar",
    rejectLabel: "Cancelar",
    accept: async () => {
      await deleteUser(id)
      await fetchUsers()
    },
    reject: () => {},
  })
}
</script>