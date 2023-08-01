import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardRoutingModule } from './dashboard-routing.module';
import { DashboardComponent } from './dashboard.component';
import { HttpClientModule } from '@angular/common/http';
import { ProfileService } from './services/profile.service';
import { StoreModule } from '@ngrx/store';
import { EffectsModule } from '@ngrx/effects';
import { ProfileEffects } from './store/profile/profile.effects';
import { reducers } from './store/reducers';


@NgModule({
    declarations: [
        DashboardComponent
    ],
    imports: [
        CommonModule,
        HttpClientModule,
        DashboardRoutingModule,
        StoreModule.forFeature("app", reducers),
        EffectsModule.forFeature([ProfileEffects])
    ],
    providers: [
        ProfileService
    ]
})
export class DashboardModule { }
