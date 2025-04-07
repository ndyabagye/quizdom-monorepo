import Layout from '@/components/modules/layout/templates'
import { AuthProvider } from '@/contexts/auth'
import { createRootRoute } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'

export const Route = createRootRoute({
  component: () => (
    <>
      <AuthProvider>
        <Layout />
        <TanStackRouterDevtools />
      </AuthProvider>
    </>
  ),
})