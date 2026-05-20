<template>
  <Form @submit="onSubmit" class="flex flex-col gap-4">

    <div class="flex flex-col gap-1.5">
      <label class="text-sm font-medium text-surface-700">Nome</label>
      <BaseInput
        :modelValue="name"
        @update:modelValue="val => emit('update:name', val)"
        placeholder="Nome"
      />
      <small v-if="errors.name" class="text-red-500 text-xs">{{ errors.name[0] }}</small>
    </div>

    <div class="flex flex-col gap-1.5">
      <label class="text-sm font-medium text-surface-700">Sobrenome</label>
      <BaseInput
        :modelValue="lastName"
        @update:modelValue="val => emit('update:lastName', val)"
        placeholder="Sobrenome"
      />
      <small v-if="errors.lastName" class="text-red-500 text-xs">{{ errors.lastName[0] }}</small>
    </div>
    
    <div class="flex gap-2 pt-2">
      <BaseButton
        type="submit"
        label="Salvar"
        icon="pi pi-check"
        :loading="loading"
      />
      <BaseButton
        type="button"
        label="Cancelar"
        icon="pi pi-times"
        severity="secondary"
        @click="emit('cancel')"
      />
    </div>

  </Form>
</template>

<script setup>
import BaseInput from '@/shared/components/base/BaseInput.vue'
import BaseButton from '@/shared/components/base/BaseButton.vue'
import { Form } from '@primevue/forms'

const emit = defineEmits(['cancel', 'update:name', 'update:lastName', 'submit'])

defineProps({
  name: String,
  lastName: String,
  loading: Boolean,
  errors: { type: Object, default: () => ({}) }
})

const onSubmit = () => emit('submit')
</script>