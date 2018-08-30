import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointState, BreakpointObserver } from '@angular/cdk/layout';

@Component({
  selector: 'app-character-sheet',
  templateUrl: './character-sheet.component.html',
  styleUrls: ['./character-sheet.component.css']
})
export class CharacterSheetComponent {
  /** Based on the screen size, switch from standard to one column per row */
  cards = this.breakpointObserver.observe(Breakpoints.Handset).pipe(
    map(({ matches }) => {
      if (matches) {
        return [
          { title: 'Card 1', cols: 13, rows: 2 },
          { title: 'Card 2', cols: 13, rows: 9 },
          { title: 'Card 3', cols: 13, rows: 4 },
          { title: 'Card 4', cols: 13, rows: 9 },
          { title: 'Card 5', cols: 13, rows: 5 },
          { title: 'Card 6', cols: 13, rows: 13 },
          { title: 'Card 7', cols: 13, rows: 13 },
          { title: 'Card 8', cols: 13, rows: 9 }
        ];
      }

      return [
        { title: 'Card 1', cols: 13, rows: 2 },
        { title: 'Card 2', cols: 5, rows: 9 },
        { title: 'Card 3', cols: 4, rows: 4 },
        { title: 'Card 4', cols: 4, rows: 9 },
        { title: 'Card 5', cols: 4, rows: 5 },
        { title: 'Card 6', cols: 5, rows: 13 },
        { title: 'Card 7', cols: 8, rows: 13 },
        { title: 'Card 8', cols: 13, rows: 9 }
      ];
    })
  );

  constructor(private breakpointObserver: BreakpointObserver) {}
}
