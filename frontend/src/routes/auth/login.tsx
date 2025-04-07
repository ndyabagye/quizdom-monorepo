import { useState } from 'react';
import { createFileRoute, Link, useNavigate } from '@tanstack/react-router'
import { useMutation } from '@tanstack/react-query';
import { z } from 'zod';
import axios from 'axios';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Form, FormControl, FormField, FormItem, FormLabel } from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';

// form validation schema
const loginSchema = z.object({
  username: z.string().min(1, { message: 'Username is required' }),
  password: z.string().min(1, { message: 'Password is required' }),
});

type LoginFormValues = z.infer<typeof loginSchema>;

export const Route = createFileRoute('/auth/login')({
  component: LoginPage,
})

function LoginPage() {
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);

  // create form 
  const form = useForm<LoginFormValues>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      username: '',
      password: '',
    },
  });

  // set up login mutation
  const loginMutation = useMutation({
    mutationFn: async (data: LoginFormValues) => {
      // For FastAPI's OAuth2PasswordRequestForm, we need to send as form data
      const formData = new URLSearchParams();
      formData.append('username', data.username);
      formData.append('password', data.password);

      const response = await axios.post('/auth/token', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      return response.data;
    },
    onSuccess: (data) => {
      // Store token in localStorage (or better, use a secure cookie or auth context)
      localStorage.setItem('token', data.access_token);
      // redirect to dashboard or home page
      navigate({ to: '/' });
    },
    onError: (error: any) => {
      setError(error.response?.data?.detail || 'Login failed !');
    }
  });

  const onSubmit = (data: LoginFormValues) => {
    setError(null); // Reset error message
    loginMutation.mutate(data);
  }

  return (
      <Card className="max-w-md mx-auto">
        <CardHeader>
          <CardTitle className="text-2xl font-semibold">Login</CardTitle>
          <CardDescription>Enter your credentials to access your account</CardDescription>
        </CardHeader>
        <CardContent>
          {error && (
            <Alert variant="destructive" className="mb-4">
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className='space-y-4'>
              <FormField
                control={form.control}
                name='username'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Username</FormLabel>
                    <FormControl>
                      <Input placeholder='Enter your username' {...field} />
                    </FormControl>
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name='password'
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Password</FormLabel>
                    <FormControl>
                      <Input type='password' placeholder='Enter your password' {...field} />
                    </FormControl>
                  </FormItem>
                )}
              />
              <Button
                type="submit"
                className='w-full'
                disabled={loginMutation.isPending}
              >
                {loginMutation.isPending ? 'Logging in...' : 'Login'}
              </Button>
            </form>
          </Form>
        </CardContent>
        <CardFooter className='flex flex-col space-y-2'>
          <div className="text-sm text-center">
            Don't have an account? <Link to="/auth/signup" className='text-blue-600 hover:underline'>Sign Up</Link>
          </div>
        </CardFooter>
      </Card>
  )
}
