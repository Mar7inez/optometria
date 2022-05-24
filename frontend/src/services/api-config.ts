const API_URL = "http://127.0.0.1:8000/api";

export interface ApiConfig {
    url: string;
    timeout: number;
}

export const DEFAULT_API_CONFIG: ApiConfig = {
    url: API_URL,
    timeout: 5000,
}