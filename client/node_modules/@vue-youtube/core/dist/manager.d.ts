import type { App } from 'vue-demi';
export declare type RegisterFunction = (data: RegisterFunctionReturn) => void;
export declare type RegisterFunctionReturn = {
    factory: any;
    id: string;
};
declare global {
    interface Window {
        onYouTubeIframeAPIReady: () => void;
        YT: any;
    }
}
export interface ManagerState {
    backlog: Map<string, RegisterFunction>;
    players: Map<string, RegisterFunction>;
    counter: number;
    factory: any;
}
export interface Manager {
    install(app: App): void;
    register(target: HTMLElement, cb: RegisterFunction): void;
    state: ManagerState;
    _insert(): void;
}
export declare const injectManager: () => Manager;
/**
 * Create a YouTube Iframe player manager. The manager provides a `install` method which gets called
 * by Vue's `app.use()`.
 *
 * @see https://vue-youtube.github.io/docs/usage/manager.html
 * @returns Manager
 */
export declare const createManager: () => Manager;
