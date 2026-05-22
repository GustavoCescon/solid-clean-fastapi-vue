<template>
  <DataTable
    :value="users"
    stripedRows
    lazy
    paginator
    :rows="size"
    :totalRecords="total"
    :rowsPerPageOptions="[5, 10, 25]"
    tableStyle="min-width: 50rem"
    paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown"
    @page="emit('page', $event)"
  >

    <Column field="id" header="ID" style="width: 5rem" />
    <Column field="name" header="Nome" />
    <Column field="lastName" header="Sobrenome" />
    <Column field="cpf" header="CPF" />

    <Column header="Endereços" style="width: 10rem">
      <template #body="{ data }">
        <BaseButton
          label="Endereços"
          icon="pi pi-map-marker"
          severity="success"
          size="small"
          outlined
          @click="emit('addresses', data.id)"
        />
      </template>
    </Column>

    <Column header="Ações" style="width: 7rem">
      <template #body="{ data }">
        <div class="flex gap-1">
          <BaseButton
            icon="pi pi-pencil"
            severity="info"
            size="small"
            rounded
            text
            v-tooltip.top="'Editar'"
            @click="emit('edit', data.id)"
          />
          <BaseButton
            icon="pi pi-trash"
            severity="danger"
            size="small"
            rounded
            text
            v-tooltip.top="'Deletar'"
            @click="emit('delete', data.id)"
          />
        </div>
      </template>
    </Column>

  </DataTable>
</template>

<script setup>
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import BaseButton from '@/shared/components/base/BaseButton.vue'

defineProps({
  users: Array,
  total: { type: Number, default: 0 },
  size: { type: Number, default: 10 },
})

const emit = defineEmits(['edit', 'delete', 'page', 'addresses'])
</script>
