import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import UsersTable from '../UsersTable.vue'

const USERS = [
  { id: 1, name: 'Alice', lastName: 'Smith' },
  { id: 2, name: 'Bob', lastName: 'Jones' },
]

const stubs = {
  DataTable: {
    template: '<div><slot /></div>',
    props: [
      'value', 'paginator', 'rows', 'totalRecords', 'lazy',
      'stripedRows', 'tableStyle', 'paginatorTemplate', 'rowsPerPageOptions',
    ],
    emits: ['page'],
  },
  Column: {
    template: `<div><slot name="body" :data="{ id: 1, name: 'Alice', lastName: 'Smith' }" /></div>`,
    props: ['field', 'header', 'style'],
  },
  BaseButton: {
    template: '<button @click="$emit(\'click\')"></button>',
    props: ['icon', 'severity', 'size', 'rounded', 'text'],
    emits: ['click'],
  },
}

const mountTable = (props = {}) =>
  mount(UsersTable, {
    props: { users: USERS, total: 2, size: 10, ...props },
    global: {
      stubs,
      directives: { tooltip: () => {} },
    },
  })

describe('UsersTable', () => {
  it('renders without crashing', () => {
    const wrapper = mountTable()
    expect(wrapper.exists()).toBe(true)
  })

  it('emits "edit" with user id when edit button is clicked', async () => {
    const wrapper = mountTable()
    const buttons = wrapper.findAll('button')

    await buttons[0].trigger('click')

    expect(wrapper.emitted('edit')).toBeTruthy()
    expect(wrapper.emitted('edit')[0]).toEqual([1])
  })

  it('emits "delete" with user id when delete button is clicked', async () => {
    const wrapper = mountTable()
    const buttons = wrapper.findAll('button')

    await buttons[1].trigger('click')

    expect(wrapper.emitted('delete')).toBeTruthy()
    expect(wrapper.emitted('delete')[0]).toEqual([1])
  })

  it('accepts users, total and size props', () => {
    const wrapper = mountTable({ users: USERS, total: 2, size: 5 })

    expect(wrapper.props('users')).toEqual(USERS)
    expect(wrapper.props('total')).toBe(2)
    expect(wrapper.props('size')).toBe(5)
  })
})
