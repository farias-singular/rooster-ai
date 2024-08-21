```csharp
namespace Project.Application.UseCases.Brands.UpdateBrand.Behaviors
{
    public class UpdateBrandAuthorizationBehavior : IPipelineBehavior<UpdateBrandCommand, UpdateBrandDto>
    {
        private readonly IAuthorizationService _authorizationService;

        public UpdateBrandAuthorizationBehavior(IAuthorizationService authorizationService)
        {
            _authorizationService = authorizationService;
        }

        public async Task<UpdateBrandDto> Handle(UpdateBrandCommand command, RequestHandlerDelegate<UpdateBrandDto> next, CancellationToken ct = default)
        {
            var user = await _authorizationService.GetUserAsync() ??
                throw new UnauthorizedAccessException("User has no authorization to execute this request!");

            return await next();
        }
    }
}
```