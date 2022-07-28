import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PupperComponent } from './components/pupper/pupper.component';
import { DanceComponent } from './components/dance/dance.component';
import { WalkComponent } from './components/walk/walk.component';


const routes: Routes = [
  { path: '', redirectTo: '/pupper', pathMatch: 'full' },
  { path: 'pupper', component: PupperComponent },
  { path: 'dance', component: DanceComponent },
  { path: 'walk', component: WalkComponent },];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
