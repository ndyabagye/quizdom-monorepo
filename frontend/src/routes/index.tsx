import HomeTemplate from '@/components/modules/home/templates'
import { createFileRoute, redirect } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  beforeLoad: async () => {
    // check if user is authenticated
    const token = localStorage.getItem('token')
    if (!token) {
      throw redirect({
        to: '/auth/login',
      })
    }
  },
  component: RouteComponent,
})

function RouteComponent() {
  return <HomeTemplate />
}
