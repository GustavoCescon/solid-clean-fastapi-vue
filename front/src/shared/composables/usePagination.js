import { ref, computed } from "vue"

export function usePagination(items, perPage = 10) {
  const page = ref(1)

  const totalPages = computed(() => {
    return Math.ceil(items.value.length / perPage)
  })

  const paginatedItems = computed(() => {
    const start = (page.value - 1) * perPage
    const end = start + perPage

    return items.value.slice(start, end)
  })

  const next = () => {
    if (page.value < totalPages.value) {
      page.value++
    }
  }

  const prev = () => {
    if (page.value > 1) {
      page.value--
    }
  }

  return {
    page,
    totalPages,
    paginatedItems,
    next,
    prev,
  }
}