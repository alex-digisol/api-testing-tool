import { createAction, props } from "@ngrx/store";
import { Profile } from "../../typedefs";


export const getProfileStart = createAction(
    "[Profile] Get Profile Start"
)

export const getProfileSuccess = createAction(
    "[Profile] Get Profile Success",
    props<{payload: Profile}>()
)

export const getProfileError = createAction(
    "[Profile] Get Profile Error",
    props<{payload: string}>()
)