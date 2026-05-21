<template>
  <AppLayout>

    <div class="mb-6">
      <BaseButton
        icon="pi pi-arrow-left"
        label="Voltar"
        text
        size="small"
        class="mb-3"
        @click="router.push('/users')"
      />
      <h1 class="text-2xl font-bold text-surface-900">Editar Usuário</h1>
      <p class="text-surface-500 text-sm mt-0.5">Atualize os dados do usuário</p>
    </div>

    <Card class="max-w-lg">
      <template #content>
        <UserForm
          :name="name"
          :lastName="lastName"
          :cpf="cpf"
          @update:name="name = $event"
          @update:lastName="lastName = $event"
          @update:cpf="onCpfInput($event)"
          @submit="update"
          @cancel="router.push('/users')"
        />
      </template>
    </Card>

  </AppLayout>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AppLayout from '@/shared/components/layout/AppLayout.vue'
import UserForm from '../components/UserForm.vue'
import Card from 'primevue/card'
import BaseButton from '@/shared/components/base/BaseButton.vue'
import { useUpdateUser } from '../composables/useUpdateUser'

const route = useRoute()
const router = useRouter()
const { name, email, lastName, cpf, update, loadUser, onCpfInput } = useUpdateUser()

onMounted(() => loadUser(route.params.id))
</script>