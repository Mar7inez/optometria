import { Api } from "./api";

export class PatientApi {
  private api: Api;

  constructor(api: Api) {
    this.api = api;
  }

  async getPatients(): Promise<any> {
    try {
      const response = await this.api.axios.get("/patients/");
      if (response.status !== 200) {
        return { kind: "error" }
      }
      return response.data;
    }
    catch (err) {
      return { kind: "bad-data" };
    }
  }
}
