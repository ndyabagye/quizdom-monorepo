import { createContext, useContext, useState, useEffect, ReactNode } from "react";
import axios from "axios";

interface User {
	username: string;
}

interface AuthContextType {
	user: User | null;
	token: string | null;
	isAuthenticated: boolean;
	login: (token: string) => void;
	logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
	const [user, setUser] = useState<User | null>(null);
	const [token, setToken] = useState<string | null>(null);
	const [isLoading, setIsLoading] = useState(true)

	// initialize auth state from local storage
	useEffect(() => {
		const storedToken = localStorage.getItem("token");
		if (storedToken) {
			setToken(storedToken);
			axios.defaults.headers.common["Authorization"] = `Bearer ${storedToken}`;
		}
		// Fetch user data if needed
		// fetchCurrentUser();
		setIsLoading(false)
	}, []);

	// function to fetch the current user using the token
	// const fetchCurrentUser = async () => {
	// 	try {
	// 		// replace with actual endpoint for fetching the current user
	// 		const response = await axios.get('users/me');
	// 		setUser(response.data)
	// 	} catch (error) {
	// 		console.error("Failed to fetch user data", error)
	// 		logout();
	// 	}
	// }

	const login = (newToken: string) => {
		localStorage.setItem('token', newToken)
		setToken(newToken)
		axios.defaults.headers.common['Authorization'] = `Bearer ${newToken}`
		//optional fetch user data after login
		//fetchCurrentUser();
	}

	const logout = () => {
		localStorage.removeItem('token');
		setToken(null)
		setUser(null)
		delete axios.defaults.headers.common['Authorization']
	}

	return (
		<AuthContext.Provider
			value={{
				user, token, isAuthenticated: !!token, login, logout
			}}
		>
			{!isLoading ? children : <div>Loading...</div>}
		</AuthContext.Provider>
	)
}

export function useAuth() {
	const context = useContext(AuthContext);
	if (context === undefined) {
		throw new Error('useAuth must be used within an AuthProvider');
	}
	return context
}