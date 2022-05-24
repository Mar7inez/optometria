import { Api } from "./api";

export class PatientApi {
  private api: Api;

  constructor(api: Api) {
    this.api = api;
  }

  async getPatients(): Promise<any> {
    try {
      const response = await this.api.axios.get("/patients/");
      return response;
    }
    catch (err) {
      return { kind: "bad-data" };
    }
  }
}
