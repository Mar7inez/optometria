import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';
import { ApiConfig, DEFAULT_API_CONFIG } from "./api-config";
import { PatientApi } from './patient';

export class Api {
  axios!: AxiosInstance;
  config: ApiConfig;

  constructor(config: ApiConfig = DEFAULT_API_CONFIG) {
    this.config = config;
  }

  setup() {
    this.axios = axios.create({
      baseURL: this.config.url,
      timeout: this.config.timeout,
      headers: {
        Accept: 'application/json',
      }
    });
  }
}

const baseApi = new Api();
baseApi.setup();
const api = {
  api: baseApi,
  patients: new PatientApi(baseApi),
}

export default api;
