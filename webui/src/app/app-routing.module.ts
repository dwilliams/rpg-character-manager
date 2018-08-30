import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CharactersComponent } from './characters/characters.component';
import { CharacterDetailComponent } from './character-detail/character-detail.component';
import { CharacterSheetComponent } from './character-sheet/character-sheet.component';

const routes: Routes = [
  {path: '', redirectTo: '/charactersheet', pathMatch: 'full'},
  {path: 'characters', component: CharactersComponent},
  {path: 'detail/:id', component: CharacterDetailComponent},
  {path: 'charactersheet', component: CharacterSheetComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
