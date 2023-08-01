import { createFeatureSelector } from "@ngrx/store";
import { AppState } from "./reducers";


export const selectState = createFeatureSelector<AppState>("app");